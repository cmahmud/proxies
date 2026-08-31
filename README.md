# SyndProxy validated proxy pool

## Current pool

- Alive now: 696
- Gold now: 455
- HTTP: 164 alive / 88 gold
- HTTPS: 111 alive / 30 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 242 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45342
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
