# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 416
- HTTP: 93 alive / 61 gold
- HTTPS: 76 alive / 24 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45510
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
