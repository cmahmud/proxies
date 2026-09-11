# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 416
- HTTP: 87 alive / 66 gold
- HTTPS: 43 alive / 19 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48855
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
