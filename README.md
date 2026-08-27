# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 406
- HTTP: 106 alive / 61 gold
- HTTPS: 171 alive / 16 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40747
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
