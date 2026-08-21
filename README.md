# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 375
- HTTP: 298 alive / 91 gold
- HTTPS: 190 alive / 22 gold
- SOCKS4: 209 alive / 126 gold
- SOCKS5: 231 alive / 136 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29826
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
