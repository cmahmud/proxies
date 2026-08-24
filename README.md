# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 415
- HTTP: 103 alive / 73 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33713
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
