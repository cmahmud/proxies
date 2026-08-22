# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 396
- HTTP: 247 alive / 90 gold
- HTTPS: 181 alive / 29 gold
- SOCKS4: 204 alive / 142 gold
- SOCKS5: 209 alive / 135 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31610
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
