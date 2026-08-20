# SyndProxy private pool

## Current pool

- Alive now: 698
- Gold now: 380
- HTTP: 165 alive / 74 gold
- HTTPS: 123 alive / 20 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 206 alive / 148 gold

## Historical pool

- Discovered: 145568
- Ever alive: 25514
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
