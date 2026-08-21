# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 393
- HTTP: 308 alive / 82 gold
- HTTPS: 175 alive / 20 gold
- SOCKS4: 241 alive / 148 gold
- SOCKS5: 230 alive / 143 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29630
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
