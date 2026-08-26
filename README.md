# SyndProxy validated proxy pool

## Current pool

- Alive now: 679
- Gold now: 399
- HTTP: 146 alive / 79 gold
- HTTPS: 187 alive / 21 gold
- SOCKS4: 170 alive / 146 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39957
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
