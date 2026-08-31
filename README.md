# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 480
- HTTP: 136 alive / 102 gold
- HTTPS: 116 alive / 43 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45060
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
