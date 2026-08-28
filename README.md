# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 410
- HTTP: 105 alive / 64 gold
- HTTPS: 104 alive / 18 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42578
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
