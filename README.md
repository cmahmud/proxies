# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 573
- HTTP: 306 alive / 189 gold
- HTTPS: 225 alive / 98 gold
- SOCKS4: 225 alive / 137 gold
- SOCKS5: 237 alive / 149 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23244
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
