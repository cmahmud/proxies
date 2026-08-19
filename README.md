# SyndProxy private pool

## Current pool

- Alive now: 1190
- Gold now: 527
- HTTP: 444 alive / 152 gold
- HTTPS: 325 alive / 107 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 203 alive / 125 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
