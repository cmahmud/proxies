# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 473
- HTTP: 148 alive / 101 gold
- HTTPS: 121 alive / 36 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45177
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
