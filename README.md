# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 400
- HTTP: 192 alive / 76 gold
- HTTPS: 166 alive / 23 gold
- SOCKS4: 217 alive / 150 gold
- SOCKS5: 203 alive / 151 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26937
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
