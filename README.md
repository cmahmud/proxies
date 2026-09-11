# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 415
- HTTP: 97 alive / 66 gold
- HTTPS: 41 alive / 20 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48872
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
