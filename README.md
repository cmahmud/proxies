# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 425
- HTTP: 308 alive / 90 gold
- HTTPS: 196 alive / 25 gold
- SOCKS4: 213 alive / 154 gold
- SOCKS5: 234 alive / 156 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30097
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
