# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 440
- HTTP: 113 alive / 82 gold
- HTTPS: 58 alive / 26 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43690
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
