# SyndProxy private pool

## Current pool

- Alive now: 814
- Gold now: 421
- HTTP: 218 alive / 87 gold
- HTTPS: 147 alive / 23 gold
- SOCKS4: 208 alive / 142 gold
- SOCKS5: 241 alive / 169 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31393
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
