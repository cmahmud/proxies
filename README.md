# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 389
- HTTP: 71 alive / 56 gold
- HTTPS: 69 alive / 13 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42863
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
