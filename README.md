# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 428
- HTTP: 325 alive / 98 gold
- HTTPS: 209 alive / 23 gold
- SOCKS4: 191 alive / 144 gold
- SOCKS5: 254 alive / 163 gold

## Historical pool

- Discovered: 153744
- Ever alive: 28760
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
