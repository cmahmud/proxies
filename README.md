# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 348
- HTTP: 188 alive / 40 gold
- HTTPS: 70 alive / 9 gold
- SOCKS4: 172 alive / 153 gold
- SOCKS5: 187 alive / 146 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32845
- Ever gold: 1213

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
