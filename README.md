# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 411
- HTTP: 115 alive / 61 gold
- HTTPS: 163 alive / 18 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41004
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
