# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 466
- HTTP: 128 alive / 93 gold
- HTTPS: 115 alive / 40 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 206 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44907
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
