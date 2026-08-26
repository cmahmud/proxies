# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 404
- HTTP: 105 alive / 64 gold
- HTTPS: 54 alive / 18 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38954
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
