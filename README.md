# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 409
- HTTP: 118 alive / 61 gold
- HTTPS: 171 alive / 15 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40807
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
