# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 450
- HTTP: 130 alive / 83 gold
- HTTPS: 121 alive / 38 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 211 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44780
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
