# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 415
- HTTP: 109 alive / 68 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35337
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
