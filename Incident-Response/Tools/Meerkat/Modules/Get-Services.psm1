function Get-Services {
    <#
    .SYNOPSIS 
        Queries the services on a given hostname, FQDN, or IP address.

    .DESCRIPTION 
        Queries the services on a given hostname, FQDN, or IP address.

        Alternative: net.exe start
        Alternative: sc.exe query
        Alternative: tasklist.exe /svc

    .EXAMPLE 
        Get-Services

    .EXAMPLE 
        Invoke-Command -ComputerName remoteHost -ScriptBlock ${Function:Get-Services} | 
        Select-Object -Property * -ExcludeProperty PSComputerName,RunspaceID | 
        Export-Csv -NoTypeInformation ("c:\temp\Services.csv")

    .EXAMPLE 
        $Targets = Get-ADComputer -filter * | Select -ExpandProperty Name
        ForEach ($Target in $Targets) {
            Invoke-Command -ComputerName $Target -ScriptBlock ${Function:Get-Services} | 
            Select-Object -Property * -ExcludeProperty PSComputerName,RunspaceID | 
            Export-Csv -NoTypeInformation ("c:\temp\" + $Target + "_Services.csv")
        }

    .NOTES 
        Updated: 2019-04-05

            Contributing Authors:
                Anthony Phipps
                
            LEGAL: Copyright (C) 2019
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.
        
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.

    .LINK
        https://github.com/TonyPhipps/Meerkat
        https://github.com/TonyPhipps/Meerkat/wiki/Services
    #>

    [CmdletBinding()]
    param(
    )

    begin{

        $DateScanned = Get-Date -Format u
        Write-Information -InformationAction Continue -MessageData ("Started Get-Services at {0}" -f $DateScanned)

        $stopwatch = New-Object System.Diagnostics.Stopwatch
        $stopwatch.Start()
    }

    process{        
            
        $ResultsArray = Get-CIMinstance -class Win32_Service -Filter "Caption LIKE '%'"
        # Odd filter explanation: http://itknowledgeexchange.techtarget.com/powershell/cim-session-oddity/
         
        foreach($Result in $ResultsArray) {
            
            $Result | Add-Member -MemberType NoteProperty -Name "Host" -Value $env:COMPUTERNAME
            $Result | Add-Member -MemberType NoteProperty -Name "DateScanned" -Value $DateScanned
        }
                
        return $ResultsArray | Select-Object Host, DateScanned, AcceptPause, AcceptStop, Caption, 
        CheckPoint, DelayedAutoStart, Description, DesktopInteract, DisconnectedSessions, DisplayName, 
        ErrorControl, ExitCode, InstallDate, Name, PathName, ProcessId, ServiceSpecificExitCode, 
        ServiceType, Started, StartMode, StartName, State, TagId, TotalSessions, WaitHint
    }

    end{

        $elapsed = $stopwatch.Elapsed

        Write-Verbose ("Total time elapsed: {0}" -f $elapsed)
        Write-Verbose ("Ended at {0}" -f (Get-Date -Format u))
    }
}