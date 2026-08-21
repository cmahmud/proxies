# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 377
- HTTP: 308 alive / 90 gold
- HTTPS: 197 alive / 25 gold
- SOCKS4: 209 alive / 127 gold
- SOCKS5: 231 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29826
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
