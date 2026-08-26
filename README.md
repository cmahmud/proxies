# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 387
- HTTP: 130 alive / 70 gold
- HTTPS: 172 alive / 20 gold
- SOCKS4: 158 alive / 145 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40000
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
