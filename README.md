# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 433
- HTTP: 96 alive / 76 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 190 alive / 170 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49090
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
