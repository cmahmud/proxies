# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 408
- HTTP: 135 alive / 72 gold
- HTTPS: 161 alive / 18 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40470
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
