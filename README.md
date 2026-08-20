# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 386
- HTTP: 229 alive / 79 gold
- HTTPS: 144 alive / 20 gold
- SOCKS4: 207 alive / 143 gold
- SOCKS5: 203 alive / 144 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25232
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
