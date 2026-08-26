# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 410
- HTTP: 131 alive / 72 gold
- HTTPS: 169 alive / 21 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40435
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
