# SyndProxy validated proxy pool

## Current pool

- Alive now: 428
- Gold now: 358
- HTTP: 59 alive / 42 gold
- HTTPS: 36 alive / 7 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 169 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43536
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
