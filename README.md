# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 415
- HTTP: 101 alive / 74 gold
- HTTPS: 117 alive / 20 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 171 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41822
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
