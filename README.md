# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 437
- HTTP: 142 alive / 82 gold
- HTTPS: 116 alive / 25 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34571
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
