# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 582
- HTTP: 310 alive / 171 gold
- HTTPS: 276 alive / 142 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 203 alive / 126 gold

## Historical pool

- Discovered: 127380
- Ever alive: 19959
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
