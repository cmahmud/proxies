# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 404
- HTTP: 87 alive / 61 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38467
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
