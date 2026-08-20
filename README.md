# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 386
- HTTP: 150 alive / 68 gold
- HTTPS: 94 alive / 19 gold
- SOCKS4: 197 alive / 154 gold
- SOCKS5: 207 alive / 145 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25697
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
