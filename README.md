# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 407
- HTTP: 104 alive / 64 gold
- HTTPS: 65 alive / 21 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38717
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
