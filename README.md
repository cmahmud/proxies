# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 407
- HTTP: 103 alive / 61 gold
- HTTPS: 83 alive / 17 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38309
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
