# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 482
- HTTP: 147 alive / 100 gold
- HTTPS: 122 alive / 43 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45104
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
