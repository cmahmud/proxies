# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 398
- HTTP: 88 alive / 56 gold
- HTTPS: 73 alive / 13 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41552
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
