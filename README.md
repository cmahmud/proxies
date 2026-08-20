# SyndProxy private pool

## Current pool

- Alive now: 630
- Gold now: 386
- HTTP: 153 alive / 65 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 199 alive / 152 gold
- SOCKS5: 198 alive / 152 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25713
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
