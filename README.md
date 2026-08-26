# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 404
- HTTP: 118 alive / 69 gold
- HTTPS: 58 alive / 17 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38942
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
