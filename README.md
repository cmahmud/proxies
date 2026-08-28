# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 391
- HTTP: 76 alive / 55 gold
- HTTPS: 69 alive / 17 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42886
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
