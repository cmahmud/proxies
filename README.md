# SyndProxy private pool

## Current pool

- Alive now: 658
- Gold now: 362
- HTTP: 159 alive / 67 gold
- HTTPS: 109 alive / 21 gold
- SOCKS4: 187 alive / 132 gold
- SOCKS5: 203 alive / 142 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25759
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
