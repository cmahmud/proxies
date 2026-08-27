# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 418
- HTTP: 102 alive / 59 gold
- HTTPS: 96 alive / 23 gold
- SOCKS4: 181 alive / 167 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41537
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
