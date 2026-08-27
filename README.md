# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 412
- HTTP: 106 alive / 64 gold
- HTTPS: 167 alive / 17 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40758
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
