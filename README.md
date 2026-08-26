# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 410
- HTTP: 133 alive / 75 gold
- HTTPS: 154 alive / 22 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40224
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
